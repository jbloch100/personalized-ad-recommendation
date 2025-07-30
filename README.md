# Personalized Ad Recommendation Engine

## Overview
Simple recommender system that tracks user-ad interactions and recommends unseen ads based on popularity.

## Features
- Records user-ad interactions
- Returns top K unseen ad recommendations
- Uses mock data for testing

## Run
```bash
python src/main.py
```

## Test
```bash
python -m unittest tests/test_main.py
```

## Docker

### Build
```bash
docker build -t personalized-ad-recommendation .
```

### Run
```bash
docker run --rm personalized-ad-recommendation
```

### Test
```bash
docker run --rm personalized-ad-recommendation python -m unittest discover -s tests
```