from products.models import Category


def get_category_emoji(category: Category):
    if 'Food' in category.name:
        return '🍔'
    elif 'Drink' in category.name:
        return '🥤'
    elif 'Toy' in category.name:
        return '🎮'
    else:
        return '📦'
