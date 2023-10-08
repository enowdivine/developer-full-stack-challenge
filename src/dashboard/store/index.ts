export const state = () => ({
    user: {},
    authors: [],
    books: [],
});

export const mutations = {
    // User Mutations
    LOGIN: (state: { user: any }, data: any) => {
        state.user = data;
        localStorage.setItem('access_token', data.access_token);
    },
    LOGOUT: (state: { user: Object }, data: Object) => {
        state.user = {};
        localStorage.removeItem('access_token');
    },

    // Authors Mutations
    ALL_AUTHORS: (state: { authors: any[] }, data: any) => {
        state.authors = data;
    },
    ADD_AUTHOR: (state: { authors: any[] }, data: Object) => {
        state.authors.unshift(data);
    },

    // Books Mutations
    ALL_BOOKS: (state: { books: any[] }, data: any) => {
        state.books = data;
    },
    ADD_BOOK: (state: { books: any[] }, data: Object) => {
        state.books.unshift(data);
    },
    DELETE_BOOK: (state: { books: any[] }, data: Object) => {
        state.books.splice(state.books.indexOf(data), 1);
    },
};
