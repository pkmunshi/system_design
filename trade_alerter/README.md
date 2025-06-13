# Trade Alerter

A secure and automated system that monitors trading posts and sends alerts via email and SMS when new content is detected.

## Features

- Automated monitoring of trading posts
- Secure email and SMS notifications
- Encrypted storage of sensitive data
- Comprehensive error handling and monitoring
- GitHub Actions integration for automated runs

## Security Features

### Data Protection
- All sensitive data is encrypted at rest
- Secure storage of credentials and configuration
- Environment variables for sensitive information
- Masked logging of sensitive data

### Error Handling & Monitoring
- Multi-level error severity tracking
- Automated email alerts for critical issues
- Detailed error context and history
- Secure error logging

### Secure Communication
- TLS encryption for email communication
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
git clone <repository-url>
cd trade_alerter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create necessary directories:
```bash
mkdir -p data logs
```

4. Set up environment variables in `.env`:
```env
# Trading Platform Credentials
TRADE_USERNAME=your_username
TRADE_PASSWORD=your_password

# Email Configuration
FROM_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
TO_SMS_NUMBER=your_phone_number
TO_EMAILS=email1@example.com,email2@example.com

# Encryption
ENCRYPTION_KEY=your_encryption_key
```

5. Generate encryption key (if not provided):
```bash
python utils/generate_key.py
```

## GitHub Actions Setup

1. Add the following secrets to your GitHub repository:
   - `TRADE_USERNAME`
   - `TRADE_PASSWORD`
   - `FROM_EMAIL`
   - `GMAIL_APP_PASSWORD`
   - `TO_SMS_NUMBER`
   - `TO_EMAILS`
   - `ENCRYPTION_KEY`

2. The workflow will run automatically every 15 minutes.

## Project Structure

```
trade_alerter/
├── .github/
│   └── workflows/
│       └── check_post.yml
├── checker/
│   ├── post_checker.py
│   └── check_chrome.py
├── utils/
│   ├── secure_storage.py
│   ├── secure_logging.py
│   ├── error_handler.py
│   └── generate_key.py
├── credentials/
│   └── config.template.json
├── data/
│   ├── last_post.enc
│   └── new_diff.enc
├── logs/
│   └── error_log.json
├── main.py
├── requirements.txt
└── README.md
```

## Security Best Practices

1. **Never commit sensitive data**:
   - Keep all credentials in environment variables
   - Use `.env` file locally (not committed)
   - Use GitHub secrets for CI/CD

2. **Regular maintenance**:
   - Monitor error logs
   - Review security alerts
   - Update dependencies regularly

3. **Access control**:
   - Restrict access to sensitive directories
   - Use proper file permissions
   - Regular audit of access logs

## Error Handling

The system implements a comprehensive error handling system with:
- Multiple severity levels (INFO, WARNING, ERROR, CRITICAL)
- Automated email alerts for critical issues
- Detailed error context and history
- Secure error logging

## Monitoring

- Check `logs/error_log.json` for error history
- Monitor email alerts for critical issues
- Review GitHub Actions logs for execution status

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
1. Check the [existing issues](https://github.com/pkmunshi/source/trade_alerter/issues) to see if your question has already been answered
2. If you find a bug or have a feature request, please [open a new issue](https://github.com/pkmunshi/source/trade_alerter/issues/new)
3. When creating an issue, please:
   - Use a clear and descriptive title
   - Include steps to reproduce the problem
   - Add any relevant error messages or logs
   - Specify your environment (OS, Python version, etc.)

For security-related issues, please email [poonam@lamba.live] instead of creating a public issue.
