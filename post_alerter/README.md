# Post Alerter

A secure and automated system for monitoring website posts and sending notifications when new content is detected.

## Features

- Automated post monitoring
- Secure notifications via email and SMS
- Encrypted data storage
- Comprehensive error handling
- GitHub Actions integration

## Security Features

### Data Protection
- All sensitive data is encrypted at rest
- Secure storage of credentials and configuration
- Environment variables for sensitive information
- Masked logging of sensitive data

### Error Handling
- Comprehensive error tracking
- Secure error logging
- Automatic error reporting
- Severity-based error handling

### Secure Communication
- Encrypted email notifications
- Secure SMS delivery
- Protected API communications

## Prerequisites

- Python 3.9 or higher
- Google Chrome browser
- Gmail account with App Password
- GitHub account (for CI/CD)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/post_alerter.git
cd post_alerter
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root with the following variables:

```env
TRADE_USERNAME=your_username
TRADE_PASSWORD=your_password
FROM_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
TO_SMS_NUMBER=your_phone_number
TO_EMAILS=email1@example.com,email2@example.com
ENCRYPTION_KEY=your_encryption_key
```

## Project Structure

```
post_alerter/
├── .github/
│   └── workflows/
│       └── check_post.yml
├── checker/
│   ├── check_chrome.py
│   └── post_checker.py
├── utils/
│   ├── error_handler.py
│   ├── secure_logging.py
│   ├── secure_storage.py
│   └── validators.py
├── data/
│   ├── last_post.enc
│   └── new_diff.enc
├── logs/
├── .env
├── .gitignore
├── config.json
├── main.py
├── requirements.txt
└── README.md
```

## Security Best Practices

1. **Environment Variables**
   - Never commit sensitive data
   - Use secure environment variables
   - Rotate credentials regularly

2. **Data Storage**
   - Encrypt sensitive data
   - Use secure file permissions
   - Regular security audits

3. **Error Handling**
   - Log errors securely
   - Implement rate limiting
   - Monitor for suspicious activity

## Error Handling

The system implements a comprehensive error handling system with:
- Error severity levels
- Secure error logging
- Automatic notifications
- Error tracking and monitoring

## Monitoring

The system is monitored through:
- GitHub Actions logs
- Secure error logs
- Email notifications
- SMS alerts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please:
1. Check existing issues
2. Open a new issue if needed
3. Include:
   - Clear title
   - Steps to reproduce
   - Environment details
   - Expected vs actual behavior

For security issues, please email directly instead of creating a public issue.
