#!/usr/bin/env python3
"""
Test script for the query parser
"""

from services.query_parser import get_parser

def test_query(query):
    """Test a query and print the results"""
    parser = get_parser()

    print(f"\n=== Testing Query ===")
    print(f"Query: {query}")
    print("=" * 50)

    result = parser.parse_query(query)

    print("API Return Values:")
    print("-" * 20)

    # Print each key-value pair with labels
    for key, value in result.items():
        if isinstance(value, list):
            if value:  # Only print if not empty
                print(f"{key}: {value}")
            else:
                print(f"{key}: []")
        elif value is not None:
            print(f"{key}: {value}")
        else:
            print(f"{key}: None")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    # Test the specific query
    test_query("Search for an employee with Python and SQL Server having over all experience 2 years")