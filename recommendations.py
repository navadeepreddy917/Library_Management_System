import sqlite3
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Connect to the existing library database
def get_connection():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(base_folder, "database", "library.db")
    return sqlite3.connect(database_path)


# Recommend books similar to the selected book
def recommend_books(book_id, limit=5):

    conn = get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # Get all books
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        conn.close()
        return []

    # Get available columns
    columns = books[0].keys()

    # Prepare book information
    documents = []

    for book in books:

        title = str(book["title"]) if "title" in columns else ""
        author = str(book["author"]) if "author" in columns else ""
        category = str(book["category"]) if "category" in columns else ""

        description = ""
        if "description" in columns and book["description"]:
            description = str(book["description"])

        text = f"{title} {author} {category} {description}"

        documents.append(text)

    # Convert book information into numerical vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    # Find the selected book
    ids = [book["id"] for book in books]

    if book_id not in ids:
        conn.close()
        return []

    selected_index = ids.index(book_id)

    # Calculate similarity
    similarity_scores = cosine_similarity(
        matrix[selected_index:selected_index + 1],
        matrix
    ).flatten()

    # Rank similar books
    ranked_books = sorted(
        [
            (i, float(similarity_scores[i]))
            for i in range(len(books))
            if ids[i] != book_id
        ],
        key=lambda x: x[1],
        reverse=True
    )[:limit]

    # Prepare results
    recommendations = []

    for index, score in ranked_books:

        book = books[index]

        recommendations.append({
            "id": book["id"],
            "title": book["title"],
            "author": book["author"],
            "category": book["category"],
            "score": round(score, 2)
        })

    conn.close()

    return recommendations