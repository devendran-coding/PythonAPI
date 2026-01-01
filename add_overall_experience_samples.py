#!/usr/bin/env python3
"""
Add training data for overall experience detection
"""

import json

# Load training data
with open('/Users/Dev/Projects/PythonAPI/data/complete_training_data.json', 'r') as f:
    data = json.load(f)

print(f"Current training data size: {len(data)}")

# Check if any samples exist with "over all experience" pattern
overall_samples = [item for item in data if "over all experience" in item[0].lower() or "overall experience" in item[0].lower()]
print(f"\nExisting overall experience samples: {len(overall_samples)}")

if overall_samples:
    print("\nFirst 3 existing samples with 'overall':")
    for sample in overall_samples[:3]:
        print(f"  - {sample}")

# Add more specific training samples for "over all experience"
new_samples = [
    [
        "Search for an employee with Python and SQL Server having over all experience 2 years",
        {"entities": [[31, 37, "TECHNOLOGY"], [42, 52, "TECHNOLOGY"], [66, 87, "OVERALL_EXPERIENCE"]]}
    ],
    [
        "Find developer with over all experience 5 years",
        {"entities": [[20, 40, "OVERALL_EXPERIENCE"], [41, 47, "OVERALL_EXPERIENCE"]]}
    ],
    [
        "Employee with Java having over all experience 3 years",
        {"entities": [[16, 20, "TECHNOLOGY"], [37, 57, "OVERALL_EXPERIENCE"]]}
    ],
    [
        "Need expert with over all experience 10 years",
        {"entities": [[18, 38, "OVERALL_EXPERIENCE"], [39, 46, "OVERALL_EXPERIENCE"]]}
    ],
]

# Check if these samples already exist
existing_queries = {item[0].lower() for item in data}

for sample in new_samples:
    if sample[0].lower() not in existing_queries:
        data.append(sample)
        print(f"\n✅ Added: {sample[0]}")
    else:
        print(f"\n⏭️  Already exists: {sample[0]}")

print(f"\nNew training data size: {len(data)}")

# Save back to file
with open('/Users/Dev/Projects/PythonAPI/data/complete_training_data.json', 'w') as f:
    json.dump(data, f)

print("\n✅ Training data updated successfully!")
