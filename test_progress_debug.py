from app import app
import re

with app.test_client() as client:
    # Login - use session_transaction to maintain session
    with client.session_transaction() as sess:
        sess['uid'] = 1
        sess['name'] = 'Sejal Singh'
    
    # Check progress page with authenticated session
    resp = client.get('/progress', follow_redirects=True)
    print(f'Progress: {resp.status_code}')
    print(f'Final path: {resp.request.path}')
    content = resp.get_data(as_text=True)
    
    # Check for key elements
    for keyword in ['trendChart', 'distChart', 'chart.umd', 'No completed interviews', 'progress-table', 'Technical']:
        if keyword in content:
            print(f'  FOUND: {keyword}')
        else:
            print(f'  MISSING: {keyword}')
    
    # Show first 3000 chars
    print(f'\nContent preview:\n{content[:3000]}')