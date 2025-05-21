from datetime import UTC, datetime, timedelta
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mail import Mail, Message
import json
import os
import uuid

app = Flask(__name__, static_folder='../landing', static_url_path='')
app.config['NEWS_FILE'] = os.getenv('NEWS_FILE', 'data/news.jsonl')
app.config['ADMIN_PASSWORD'] = os.getenv('ADMIN_PASSWORD', 'changeme')
app.config['CONTACT_FILE'] = os.getenv('CONTACT_FILE', 'data/contact.jsonl')
app.config['NEWSLETTER_FILE'] = os.getenv('NEWSLETTER_FILE', 'data/newsletter.jsonl')
app.config['ROADMAP_FILE'] = os.getenv('ROADMAP_FILE', 'data/roadmap.jsonl')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email address
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', app.config['MAIL_USERNAME'])
app.config['MAIL_RECIPIENT'] = os.getenv('MAIL_RECIPIENT', app.config['MAIL_USERNAME'])
limiter = Limiter(app=app, key_func=get_remote_address)
mail = Mail(app)
CORS(app)

TOKENS = {}

def load_news():
    if not os.path.exists(app.config['NEWS_FILE']):
        return []
    with open(app.config['NEWS_FILE']) as f:
        return [json.loads(line) for line in f]

def save_news(item):
    with open(app.config['NEWS_FILE'], 'a') as f:
        f.write(json.dumps(item) + '\n')
        
@app.route('/api/news', methods=['GET'])
def get_news():
    return jsonify(load_news())

@app.route('/api/news', methods=['POST'])
def post_news():
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token, None)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.json
    item = {
        'id': str(uuid.uuid4()),
        'title': data.get('title', '').strip(),
        'date': data.get('date', '').strip(),
        'content': data.get('content', '').strip()
    }
    if not item['title'] or not item['date'] or not item['content']:
        return jsonify({'error': 'Missing fields'}), 400
    save_news(item)
    return jsonify(item), 201

@app.route('/api/news/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token, None)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401
    news_items = load_news()
    updated_news = [item for item in news_items if item.get('id') != news_id]
    if len(news_items) == len(updated_news):
        return jsonify({'error': 'News item not found'}), 404
    with open(app.config['NEWS_FILE'], 'w') as f:
        for item in updated_news:
            f.write(json.dumps(item) + '\n')
    return jsonify({'success': True})

@app.route('/api/news/<news_id>', methods=['PUT'])
def update_news(news_id):
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token, None)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.json
    title = data.get('title', '').strip()
    date = data.get('date', '').strip()
    content = data.get('content', '').strip()
    if not title or not date or not content:
        return jsonify({'error': 'Missing fields'}), 400
    news_items = load_news()
    updated = False
    for item in news_items:
        if item.get('id') == news_id:
            item['title'] = title
            item['date'] = date
            item['content'] = content
            updated = True
            break
    if not updated:
        return jsonify({'error': 'News item not found'}), 404
    with open(app.config['NEWS_FILE'], 'w') as f:
        for item in news_items:
            f.write(json.dumps(item) + '\n')
    return jsonify({'success': True})

def load_roadmap():
    if not os.path.exists(app.config['ROADMAP_FILE']):
        return []
    with open(app.config['ROADMAP_FILE']) as f:
        return [json.loads(line) for line in f]

def save_roadmap(items):
    with open(app.config['ROADMAP_FILE'], 'w') as f:
        for item in items:
            f.write(json.dumps(item) + '\n')

@app.route('/api/roadmap', methods=['GET'])
def get_roadmap():
    return jsonify(load_roadmap())

@app.route('/api/roadmap', methods=['POST'])
def post_roadmap():
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json
    item = {
        'id': str(uuid.uuid4()),
        'title': data.get('title', '').strip(),
        'quarter': data.get('quarter', '').strip(),
        'description': data.get('description', '').strip(),
        'status': data.get('status', '').strip(),
    }
    if not item['title'] or not item['quarter'] or not item['description']:
        return jsonify({'error': 'Missing required fields'}), 400

    items = load_roadmap()
    items.append(item)
    save_roadmap(items)
    return jsonify(item), 201

@app.route('/api/roadmap/<roadmap_id>', methods=['PUT'])
def update_roadmap(roadmap_id):
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json
    items = load_roadmap()
    updated = False

    for item in items:
        if item.get('id') == roadmap_id:
            item['title'] = data.get('title', '').strip()
            item['quarter'] = data.get('quarter', '').strip()
            item['description'] = data.get('description', '').strip()
            item['status'] = data.get('status', '').strip()
            updated = True
            break

    if not updated:
        return jsonify({'error': 'Roadmap item not found'}), 404

    save_roadmap(items)
    return jsonify({'success': True})

@app.route('/api/roadmap/<roadmap_id>', methods=['DELETE'])
def delete_roadmap(roadmap_id):
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    token_expiry = TOKENS.get(token)
    if not token_expiry or datetime.now(UTC) > token_expiry:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401

    items = load_roadmap()
    updated_items = [item for item in items if item.get('id') != roadmap_id]

    if len(updated_items) == len(items):
        return jsonify({'error': 'Roadmap item not found'}), 404

    save_roadmap(updated_items)
    return jsonify({'success': True})

@app.route('/api/roadmap/order', methods=['POST'])
def reorder_roadmap():
    auth = request.headers.get('Authorization', '')
    token = auth.replace('Bearer ', '')
    if not TOKENS.get(token) or datetime.now(UTC) > TOKENS[token]:
        TOKENS.pop(token, None)
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json
    new_order = data.get('order', [])
    if not isinstance(new_order, list):
        return jsonify({'error': 'Invalid format'}), 400

    current_items = load_roadmap()
    id_map = {item['id']: item for item in current_items}
    reordered = [id_map[i] for i in new_order if i in id_map]

    # Keep unlisted items (optional)
    extras = [item for item in current_items if item['id'] not in new_order]
    save_roadmap(reordered + extras)

    return jsonify({'success': True})

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = request.json
    password = data.get('password')
    if password == app.config['ADMIN_PASSWORD']:
        token = str(uuid.uuid4())
        TOKENS[token] = datetime.now(UTC) + timedelta(hours=1)
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid password'}), 403

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()
    if not name or not email or not subject or not message:
        return jsonify({'error': 'All fields are required.'}), 400
    timestamp = datetime.now(UTC).isoformat()
    entry = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message,
        "timestamp": timestamp
    }
    with open(app.config['CONTACT_FILE'], 'a') as f:
        f.write(json.dumps(entry) + '\n')
    try:
        msg = Message(subject=f"[DFM] Contact: {subject}",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[app.config['MAIL_RECIPIENT']])
        msg.body = f"""
New contact form submission:

Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}

Timestamp: {timestamp}
"""
        mail.send(msg)
    except Exception as e:
        return jsonify({'error': f'Failed to send email: {str(e)}'}), 500
    return jsonify({'success': True, 'message': 'Message received and email sent.'}), 200

@app.route('/api/newsletter', methods=['POST'])
def newsletter():
    data = request.json
    email = data.get('email', '').strip()
    consent = data.get('consent', False)
    timestamp = datetime.now(UTC).isoformat()
    if not email:
        return jsonify({'error': 'Email is required.'}), 400
    if not consent:
        return jsonify({'error': 'You must provide GDPR consent to subscribe.'}), 400
    entry = {
        "email": email,
        "consent": True,
        "timestamp": timestamp
    }
    with open(app.config['NEWSLETTER_FILE'], 'a') as f:
        f.write(json.dumps(entry) + '\n')
    try:
        msg = Message(subject=f"[DFM] Newsletter: signup {email}",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[app.config['MAIL_RECIPIENT']])
        msg.body = f"""
New newsletter signup:
Email: {email}
Timestamp: {timestamp}
GDPR Consent: Yes
"""
        mail.send(msg)
    except Exception as e:
        return jsonify({'error': f'Failed to send email: {str(e)}'}), 500
    return jsonify({'success': True, 'message': 'Subscription successful with GDPR consent.'}), 200

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'landing.html')

@app.route('/js/config.js')
def config():
    return send_from_directory(app.static_folder, 'js/config_flask.js')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
