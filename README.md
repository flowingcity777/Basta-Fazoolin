# Basta Fazoolin' — Restaurant Management System

A Python-based backend system utilizing Object-Oriented Programming (OOP) to manage menus, franchise locations, and overarching corporate business structures for a restaurant group.

## Features
- **Dynamic Menu Selection:** Automatically checks and filters available menus based on specific military time frames.
- **Bill Calculation:** Looks up menu item prices within a system dictionary and returns the exact total cost for a customer order.
- **Franchise & Business Scalability:** Uses distinct classes to group menus into individual restaurant locations (Franchises) and organize those locations under parent corporate entities (Businesses).

## Code Structure
The project uses three main classes to organize data:

1. **`Menu`**: Stores the name, item prices, start time, and end time for individual menus (e.g., Brunch, Dinner, Kids). Includes functionality to calculate customer bills.
2. **`Franchise`**: Represents a specific physical address and tracks which menus are available at that location given a specific time.
3. **`Business`**: Acts as the top-level corporate structure, managing the business name and its associated franchise locations.

## How It Works
The program processes time queries using a standard 4-digit military format integer (e.g., `1200` for 12:00 PM, `1600` for 4:00 PM) to safely handle logical comparisons without string parsing errors.

```python
# Example Usage:
# Fetching menus available at a flagship store at 12:00 PM
print(flagship_store.available_menus(1200))
