# Decay Service

A microservice that implements an exponential decay scoring system for tracking trending items. The service uses Redis as a backend to store and calculate time-weighted scores for items, making it perfect for implementing trending features in applications.

## Features

- Exponential decay scoring system
- RESTful API endpoints for adding events and retrieving trending items
- Redis-backed storage for efficient score calculations
- Docker support for easy deployment
- Configurable decay rate and scoring parameters

## Prerequisites

- Docker and Docker Compose
- Python 3.6+
- Redis (included in Docker setup)

## Installation

1. Clone the repository
2. Navigate to the decay service directory
3. Build and start the containers:

```bash
docker-compose up --build
```

## Configuration

The service can be configured through environment variables:

- `REDIS_HOST`: Redis host (default: localhost)
- `REDIS_PORT`: Redis port (default: 6379)
- `REDIS_DB`: Redis database number (default: 0)
- `DECAY_RATE`: Rate at which scores decay (default: 0.001)

## API Endpoints

### Add Event

```
POST /add_event
```

Add a new event to the trending system.

Request body:
```json
{
    "item_id": "string",
    "event_time": "integer (unix timestamp)",
    "weight": "float (optional, default: 1.0)"
}
```

### Get Trending Items

```
GET /trending?count=10
```

Retrieve the top trending items.

Query parameters:
- `count`: Number of items to return (default: 10)

Response:
```json
[
    {
        "item_id": "string",
        "score": "float"
    }
]
```

## How It Works

The service implements an exponential decay scoring system where:

1. Each event is assigned a weight (default: 1.0)
2. Scores decay exponentially over time using the formula: `score = weight * exp(-decay_rate * elapsed_time)`
3. Items are stored in a Redis sorted set, automatically sorted by their decayed scores
4. The most recent and frequent events will have higher scores

## Development

To run the service locally without Docker:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Redis server

3. Run the service:
```bash
python app.py
```

## Testing

The service includes example code in `trending_exp_decay.py` that demonstrates the core functionality. You can run it to see how the decay scoring works with sample data.

## License

[Add your license information here] 