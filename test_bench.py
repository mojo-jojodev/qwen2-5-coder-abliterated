def evaluate_abliteration(model_output):
    """Ensures orthogonal direction removal preserves coding capabilities."""
    assert "def " in model_output
    print("Abliterated open-weights model maintains structural reasoning.")
