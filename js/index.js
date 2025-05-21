document.addEventListener('DOMContentLoaded', () => {
    let authToken = '';

    // API Endpoints
    if (API_VERSION !== 'v1') {
        console.error(`API version mismatch. Expecting v1 but got '${API_VERSION}'. Cross fingers!`);
    }
    const CONTACT_API = `${API}/contact`;
    const LOGIN_API = `${API}/login`;
    const NEWS_API = `${API}/news`;
    const NEWSLETTER_API = `${API}/newsletter`;
    const ROADMAP_API = `${API}/roadmap`;

    // Elements
    const $ = id => document.getElementById(id);
    const newsContainer = $('news-container');
    const addNewsBtn = $('add-news-btn');
    const newsForm = $('news-form');
    const newsItemForm = $('news-item-form');
    const cancelNews = $('cancel-news');
    const notification = $('notification');

    /** ------------------- Utility Functions ------------------- */

    const showNotification = (msg, type = 'info', duration = 3000) => {
        const base = "fixed top-6 right-6 px-4 py-2 rounded-lg shadow-lg z-50";
        const styles = {
            info: "bg-dfmTeal text-white",
            error: "bg-red-600 text-white",
            success: "bg-green-600 text-white"
        };
        notification.className = `${base} ${styles[type] || styles.info}`;
        notification.textContent = msg;
        notification.classList.remove('hidden');
        setTimeout(() => notification.classList.add('hidden'), duration);
    };

    const formatDate = dateStr => new Date(dateStr).toLocaleDateString('en-US', {
        year: 'numeric', month: 'long', day: 'numeric'
    });

    const sanitizeHTML = input => {
        const allowed = ['br', 'b', 'i', 'em', 'strong', 'a', 'ul', 'ol', 'li', 'p'];
        const template = document.createElement('template');
        template.innerHTML = input;
        const walker = document.createTreeWalker(template.content, NodeFilter.SHOW_ELEMENT, {
            acceptNode: node => allowed.includes(node.nodeName.toLowerCase())
                ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT
        });
        let node;
        while (node = walker.nextNode()) {
            [...node.attributes].forEach(attr => {
                if (node.nodeName.toLowerCase() === 'a' && attr.name === 'href') return;
                node.removeAttribute(attr.name);
            });
        }
        return template.innerHTML;
    };

    const truncateHTML = (html, maxChars = 140) => {
        const template = document.createElement('template');
        template.innerHTML = html;
        let count = 0;
        const output = document.createElement('div');

        const traverse = (node, parent) => {
            if (count >= maxChars) return;
            if (node.nodeType === Node.TEXT_NODE) {
                const text = node.textContent.slice(0, maxChars - count);
                count += text.length;
                parent.appendChild(document.createTextNode(text));
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                const clone = document.createElement(node.tagName);
                [...node.attributes].forEach(attr => {
                    if (node.tagName === 'A' && attr.name === 'href') {
                        clone.setAttribute(attr.name, attr.value);
                    }
                });
                parent.appendChild(clone);
                [...node.childNodes].forEach(child => traverse(child, clone));
            }
        };

        [...template.content.childNodes].forEach(child => traverse(child, output));
        const span = document.createElement('span');
        span.textContent = '...';
        (output.lastElementChild || output).appendChild(span);
        return output.innerHTML;
    };

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    /** ------------------- Menu Logic ------------------- */

    const mobileMenuBtn = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuBtn?.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    document.querySelectorAll('#mobile-menu a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });

    /** ------------------- News Logic ------------------- */

    const fetchNews = async () => {
        try {
            const res = await fetch(NEWS_API);
            const data = await res.json();
            data.sort((a, b) => new Date(b.date) - new Date(a.date));
            renderNews(data);
        } catch (err) {
            console.error(err);
            showNotification('Failed to fetch news.', 'error');
        }
    };

    const renderNews = newsList => {
        newsContainer.innerHTML = '';
        newsList.forEach(news => newsContainer.appendChild(createNewsItem(news)));
    };

    const createNewsItem = news => {
        const div = document.createElement('div');
        div.className = 'news-item bg-white/90 rounded-xl overflow-hidden shadow-md hover:shadow-lg relative';
        const sanitized = sanitizeHTML(news.content);
        const isLong = news.content.replace(/<[^>]*>/g, '').length > 140;
        const preview = isLong ? truncateHTML(sanitized, 140) : sanitized;

        div.innerHTML = `
            ${authToken ? createButton('delete', news.id) + createButton('edit', news) : ''}
            <div class="p-6">
                <div class="flex justify-between items-start mb-2">
                    <h3 class="text-xl font-bold text-dfmBlue">${news.title}</h3>
                    <span class="text-sm text-gray-500">${formatDate(news.date)}</span>
                </div>
                <div class="relative">
                    <div class="content-wrapper" data-full="${encodeURIComponent(sanitized)}"
                         data-truncated="${encodeURIComponent(preview)}" data-expanded="false">
                        <div class="text-gray-700 content-text">${preview}</div>
                    </div>
                    ${isLong ? `<button class="toggle-content-btn mt-2 text-dfmTeal hover:text-dfmBlue font-medium">Read more</button>` : ''}
                </div>
            </div>`;
        return div;
    };

    const createButton = (type, data) => {
        if (type === 'delete') {
            return `<button class="delete-news absolute top-2 right-2 w-6 h-6 rounded-full bg-red-100 hover:bg-red-200 text-red-600 hover:text-red-800 flex items-center justify-center text-lg font-bold" data-id="${data}" title="Delete News">&times;</button>`;
        } else if (type === 'edit') {
            return `<button class="edit-news absolute top-10 right-2 w-6 h-6 rounded-full bg-yellow-100 hover:bg-yellow-200 text-yellow-600 hover:text-yellow-800 flex items-center justify-center text-lg font-bold" data-id="${data.id}" data-title="${encodeURIComponent(data.title)}" data-date="${data.date}" data-content="${encodeURIComponent(data.content)}" title="Edit News">✎</button>`;
        }
    };

    /** ------------------- Roadmap Logic ------------------- */

    const roadmapContainer = document.getElementById('roadmap-container');
    const addRoadmapBtn = document.getElementById('add-roadmap-btn');
    const roadmapForm = document.getElementById('roadmap-form');
    const roadmapItemForm = document.getElementById('roadmap-item-form');
    const cancelRoadmap = document.getElementById('cancel-roadmap');

    async function fetchRoadmapItems() {
        try {
            const response = await fetch(ROADMAP_API); // Adjust endpoint to match your backend
            const data = await response.json();
            renderRoadmapItems(data);
        } catch (error) {
            console.error("Failed to load roadmap items:", error);
        }
    }

    function renderRoadmapItems(items) {
        roadmapContainer.innerHTML = '';

        const statusColorMap = {
            'Completed': 'bg-dfmGreen',
            'In Progress': 'bg-yellow-500',
            'Planned': 'bg-dfmBlue'
        };

        items.forEach(item => {
            const statusBadge = item.status
                ? `<span class="inline-block ${statusColorMap[item.status] || 'bg-gray-300'} text-white text-xs px-2 py-1 rounded mr-2">${item.status}</span>`
                : '';
            const adminButtons = authToken ? `
                <div class="absolute top-2 right-2 flex flex-col space-y-2 items-end">
                    <button class="delete-roadmap w-6 h-6 rounded-full bg-red-100 hover:bg-red-200 text-red-600 hover:text-red-800 flex items-center justify-center text-lg font-bold"
                        title="Delete" data-id="${item.id}">&times;</button>
                    <button class="edit-roadmap w-6 h-6 rounded-full bg-yellow-100 hover:bg-yellow-200 text-yellow-600 hover:text-yellow-800 flex items-center justify-center text-lg font-bold"
                        title="Edit"
                        data-id="${item.id}"
                        data-title="${encodeURIComponent(item.title)}"
                        data-quarter="${encodeURIComponent(item.quarter)}"
                        data-description="${encodeURIComponent(item.description)}"
                        data-status="${item.status || ''}">
                        ✎
                    </button>
                </div>
            ` : '';

            const itemHTML = `
            <div class="roadmap-item relative pl-10 bg-gray-100 p-6 rounded-lg shadow mb-6">
                ${adminButtons}
                <div class="flex justify-between items-center mb-2">
                    <h3 class="text-xl font-bold text-dfmBlue">${item.title}</h3>
                    <span class="bg-dfmBlue text-white text-sm px-3 py-1 rounded-full">${item.quarter}</span>
                </div>
                <p class="text-gray-700">${item.description}</p>
                <div class="mt-4">${statusBadge}</div>
            </div>
        `;

            roadmapContainer.insertAdjacentHTML('beforeend', itemHTML);
        });
        let roadmapSortable;
        function initRoadmapDragAndDrop() {
            if (roadmapSortable) roadmapSortable.destroy(); // Re-init safety
            roadmapSortable = Sortable.create(document.getElementById('roadmap-container'), {
                animation: 150,
                handle: '.roadmap-item', // allow drag on the item itself
                onEnd: saveRoadmapOrder
            });
        }
        if (authToken) initRoadmapDragAndDrop();
    }

    async function saveRoadmapOrder() {
        const items = Array.from(document.querySelectorAll('#roadmap-container .roadmap-item'));
        const newOrder = items.map(el => el.querySelector('.edit-roadmap')?.dataset.id || el.querySelector('.delete-roadmap')?.dataset.id);

        try {
            const res = await fetch(`${ROADMAP_API}/order`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify({ order: newOrder })
            });

            if (!res.ok) {
                const err = await res.json();
                showNotification(err.error || 'Failed to save order', 'error');
            } else {
                showNotification('Roadmap order saved', 'success');
            }
        } catch (err) {
            console.error(err);
            showNotification('Network error saving order', 'error');
        }
    }

    addRoadmapBtn.addEventListener('click', () => {
        if (!authToken) return login();
        roadmapItemForm.reset();
        document.getElementById('roadmap-submit-btn').textContent = 'Add Roadmap Item';
        delete addRoadmapBtn.dataset.editing;
        roadmapForm.classList.remove('hidden');
        addRoadmapBtn.classList.add('hidden');
    });

    cancelRoadmap.addEventListener('click', () => {
        roadmapForm.classList.add('hidden');
        addRoadmapBtn.classList.remove('hidden');
        showNotification('Roadmap form cancelled');
    });

    roadmapItemForm.addEventListener('submit', async e => {
        e.preventDefault();
        const title = document.getElementById('roadmap-title').value.trim();
        const quarter = document.getElementById('roadmap-quarter').value.trim();
        const description = document.getElementById('roadmap-description').value.trim();
        const status = document.getElementById('roadmap-status').value;

        if (!title || !quarter || !description) {
            return showNotification('All fields except status are required', 'error');
        }

        const body = { title, quarter, description, status };
        const editingId = addRoadmapBtn.dataset.editing;
        const method = editingId ? 'PUT' : 'POST';
        const url = editingId ? `${ROADMAP_API}/${editingId}` : ROADMAP_API;

        try {
            const res = await fetch(url, {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify(body)
            });
            const data = await res.json();
            if (res.ok) {
                roadmapForm.classList.add('hidden');
                addRoadmapBtn.classList.remove('hidden');
                roadmapItemForm.reset();
                fetchRoadmapItems();
                showNotification(editingId ? 'Roadmap updated!' : 'Roadmap item added!', 'success');
            } else {
                showNotification(data.error || 'Save failed', 'error');
            }
        } catch (err) {
            showNotification('Network error', 'error');
        }
    });

    /** ------------------- Event Handlers ------------------- */

    // Delegated Click Events
    document.addEventListener('click', async e => {
        const target = e.target;

        if (target.matches('.delete-news')) {
            handleDeletePrompt(target.dataset.id);
        } else if (target.matches('#confirm-delete')) {
            await handleDeleteConfirm();
        } else if (target.matches('#cancel-delete')) {
            $('delete-confirmation-modal').classList.add('hidden');
        } else if (target.matches('.edit-news')) {
            handleEditNews(target);
        } else if (target.matches('.toggle-content-btn')) {
            toggleContent(target);
        }
    });

    const handleDeletePrompt = id => {
        $('delete-confirmation-modal').classList.remove('hidden');
        $('confirm-delete').dataset.id = id;
    };

    const handleDeleteConfirm = async () => {
        const id = $('confirm-delete').dataset.id;
        if (!id) return;
        try {
            const res = await fetch(`${NEWS_API}/${id}`, {
                method: 'DELETE',
                headers: { 'Authorization': `Bearer ${authToken}` }
            });
            const result = await res.json();
            if (res.ok) {
                showNotification('News deleted', 'success');
                fetchNews();
            } else {
                showNotification(`Error: ${result.error}`, 'error');
            }
        } catch (err) {
            console.error(err);
            showNotification('Error deleting news', 'error');
        } finally {
            $('delete-confirmation-modal').classList.add('hidden');
        }
    };

    const handleEditNews = btn => {
        $('news-title').value = decodeURIComponent(btn.dataset.title);
        $('news-date').value = btn.dataset.date;
        $('news-content').value = decodeURIComponent(btn.dataset.content);
        addNewsBtn.dataset.editing = btn.dataset.id;
        $('news-submit-btn').textContent = 'Update News';
        addNewsBtn.classList.add('hidden');
        newsForm.classList.remove('hidden');
        if (!isElementInViewport(newsForm)) {
            newsForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };

    const toggleContent = btn => {
        const wrapper = btn.closest('.relative').querySelector('.content-wrapper');
        const text = wrapper.querySelector('.content-text');
        const expanded = wrapper.dataset.expanded === 'true';
        text.innerHTML = decodeURIComponent(expanded ? wrapper.dataset.truncated : wrapper.dataset.full);
        wrapper.dataset.expanded = (!expanded).toString();
        btn.textContent = expanded ? 'Read more' : 'Read less';
    };

    // News Form
    addNewsBtn.addEventListener('click', () => {
        if (!authToken) return login();
        newsForm.classList.toggle('hidden');
        $('news-submit-btn').textContent = 'Add News';
        addNewsBtn.classList.add('hidden');
        addNewsBtn.dataset.editing && delete addNewsBtn.dataset.editing;
        newsItemForm.reset();
        $('news-date').value = new Date().toISOString().split('T')[0];
    });

    cancelNews.addEventListener('click', () => {
        newsForm.classList.add('hidden');
        addNewsBtn.classList.remove('hidden');
        showNotification('News form cancelled.');
    });

    newsItemForm.addEventListener('submit', async e => {
        e.preventDefault();
        const title = $('news-title').value.trim();
        const date = $('news-date').value;
        const content = $('news-content').value.trim();
        const id = addNewsBtn.dataset.editing;
        if (!title || !date || !content) return showNotification('All fields required', 'error');

        const method = id ? 'PUT' : 'POST';
        const url = id ? `${NEWS_API}/${id}` : NEWS_API;

        try {
            const res = await fetch(url, {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authToken}`
                },
                body: JSON.stringify({ title, date, content })
            });
            const data = await res.json();
            if (res.ok) {
                fetchNews();
                newsForm.classList.add('hidden');
                addNewsBtn.classList.remove('hidden');
                newsItemForm.reset();
                showNotification(id ? 'News updated!' : 'News posted!', 'success');
            } else {
                showNotification('Error: ' + data.error, 'error');
            }
        } catch (err) {
            console.error(err);
            showNotification('Network error', 'error');
        }
    });

    document.addEventListener('click', async e => {
        const target = e.target;

        if (target.matches('.delete-roadmap')) {
            const id = target.dataset.id;
            if (confirm('Delete this roadmap item?')) {
                try {
                    const res = await fetch(`${ROADMAP_API}/${id}`, {
                        method: 'DELETE',
                        headers: { 'Authorization': `Bearer ${authToken}` }
                    });
                    if (res.ok) {
                        fetchRoadmapItems();
                        showNotification('Roadmap item deleted', 'success');
                    } else {
                        const err = await res.json();
                        showNotification(err.error || 'Delete failed', 'error');
                    }
                } catch (err) {
                    showNotification('Network error', 'error');
                }
            }
        }

        if (target.matches('.edit-roadmap')) {
            addRoadmapBtn.dataset.editing = target.dataset.id;
            document.getElementById('roadmap-title').value = decodeURIComponent(target.dataset.title);
            document.getElementById('roadmap-quarter').value = decodeURIComponent(target.dataset.quarter);
            document.getElementById('roadmap-description').value = decodeURIComponent(target.dataset.description);
            document.getElementById('roadmap-status').value = target.dataset.status;
            document.getElementById('roadmap-submit-btn').textContent = 'Update Roadmap Item';
            addRoadmapBtn.classList.add('hidden');
            roadmapForm.classList.remove('hidden');
            if (!isElementInViewport(roadmapForm)) {
                roadmapForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    });

    /** ------------------- Authentication ------------------- */

    const login = () => {
        $('admin-login-modal').classList.remove('hidden');
        setTimeout(() => $('admin-password').focus(), 0);
    };

    const handleLogin = async () => {
        const password = $('admin-password').value.trim();
        if (!password) return;
        try {
            const res = await fetch(LOGIN_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ password })
            });
            const data = await res.json();
            if (res.ok) {
                authToken = data.token;
                $('admin-login-modal').classList.add('hidden');
                $('admin-password').value = '';
                $('admin-login-label').textContent = '[Logout]';
                $('mobile-admin-login-label').textContent = '[Logout]';
                addNewsBtn.classList.remove('hidden');
                addRoadmapBtn.classList.remove('hidden');
                showNotification('Login successful', 'success');
                fetchNews();
                fetchRoadmapItems();
            } else {
                $('admin-login-error').textContent = data.error;
                $('admin-login-error').classList.remove('hidden');
            }
        } catch {
            $('admin-login-error').textContent = 'Login failed';
            $('admin-login-error').classList.remove('hidden');
        }
    };

    $('admin-login-link').addEventListener('click', e => {
        e.preventDefault();
        const label = $('admin-login-label');
        if (label.textContent === '[Logout]') {
            authToken = '';
            label.textContent = '[Admin]';
            $('mobile-admin-login-label').textContent = '[Admin]';
            addNewsBtn.classList.add('hidden');
            addRoadmapBtn.classList.add('hidden');
            showNotification('Logged out', 'success');
            fetchNews();
            fetchRoadmapItems();
        } else {
            login();
        }
    });

    $('mobile-admin-login-link').addEventListener('click', e => {
        e.preventDefault();
        $('admin-login-link').click(); // trigger the main logic
    });

    $('admin-login-submit').addEventListener('click', handleLogin);

    $('admin-password').addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleLogin();
        }
    });

    document.addEventListener('click', e => {
        if (e.target.id === 'admin-login-modal') {
            $('admin-login-modal').classList.add('hidden');
        }
    });

    /** ------------------- Contact Form ------------------- */

    document.getElementById('contact-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value.trim();
        if (!name || !email || !subject || !message) {
            showNotification('All fields are required.', 'error');
            return;
        }
        try {
            const res = await fetch(CONTACT_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, subject, message })
            });
            const result = await res.json();
            if (res.ok) {
                showNotification('Message sent successfully!', 'success');
                e.target.reset();
            } else {
                showNotification('Error sending message: ' + result.error, 'error');
            }
        } catch (err) {
            console.error(err);
            showNotification('Network error. Please try again later.', 'error');
        }
    });

    /** ------------------- Newsletter Form ------------------- */

    document.getElementById('newsletter-submit').addEventListener('click', async () => {
        const emailInput = document.getElementById('newsletter-email');
        const consentCheckbox = document.getElementById('newsletter-consent');
        const email = emailInput.value.trim();
        const consent = consentCheckbox.checked;
        if (!email) {
            showNotification('Email is required.', 'error');
            return;
        }
        if (!consent) {
            showNotification('You must agree to the privacy policy.', 'error');
            return;
        }
        try {
            const res = await fetch(NEWSLETTER_API, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, consent })
            });
            const result = await res.json();
            if (res.ok) {
                showNotification('Subscription successful!', 'success');
                emailInput.value = '';
                consentCheckbox.checked = false;
            } else {
                showNotification('Error subscribing: ' + result.error, 'error');
            }
        } catch (e) {
            console.error(e);
            showNotification('Network error. Please try again later.', 'error');
        }
    });

    /** ------------------- Initial Load ------------------- */

    fetchNews();
    fetchRoadmapItems();

});
