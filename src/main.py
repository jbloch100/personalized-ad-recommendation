from collections import defaultdict
import random

class Recommender:
    def __init__(self):
        self.user_history = defaultdict(set)
        self.item_scores = defaultdict(int)

    def record_interaction(self, user_id, item_id):
        self.user_history[user_id].add(item_id)
        self.item_scores[item_id] += 1

    def recommend(self, user_id, top_k=3):
        seen = self.user_history[user_id]
        candidates = {item: score for item, score in self.item_scores.items() if item not in seen}
        ranked = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
        return [item for item, _ in ranked[:top_k]]

def mock_data():
    users = ['u1', 'u2', 'u3']
    items = ['ad1', 'ad2', 'ad3', 'ad4', 'ad5']
    return [(random.choice(users), random.choice(items)) for _ in range(30)]

if __name__ == "__main__":
    recommender = Recommender()
    for user_id, item_id in mock_data():
        recommender.record_interaction(user_id, item_id)
    for user in ['u1', 'u2', 'u3']:
        print(f"Recommendations for {user}:", recommender.recommend(user))
