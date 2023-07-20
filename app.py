import streamlit as st
import pickle
# import pandas as pd

books_list = pickle.load(open('books.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(book):
    book_index = books_list[books_list['book_title'] == book].index[0]
    dist = similarity[book_index]
    bookslist = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    
    suggested = []
    picture = []
    for i in bookslist:
        suggested.append(books_list.iloc[i[0]].book_title)

    for i in bookslist:
        picture.append(books_list.iloc[i[0]].image_url)

    return suggested,picture


bookslist = books_list['book_title'].values
st.title('Book Recommender System')
selected_book = st.selectbox(
    'Select the book of your interest',
    books_list
)

if st.button('Recommend'):
    names,imgs = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        st.write(names[i])
        st.image(imgs[i]) 
