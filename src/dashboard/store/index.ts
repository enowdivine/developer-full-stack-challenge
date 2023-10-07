export const state = () => ({
    user: {},
    authors: [
        {
            id: 1,
            author_name: 'James cameron',
            number_of_books: 1,
        },
        {
            id: 2,
            author_name: 'Mike Scott',
            number_of_books: 1,
        },
        {
            id: 3,
            author_name: 'Fred Humphry',
            number_of_books: 1,
        },
        {
            id: 4,
            author_name: 'Tom Craiges',
            number_of_books: 1,
        },
    ],
    books: [
        {
            id: 1,
            book_name: 'Meet Uncle Dave',
            author_name: 'Fred Humphry',
            number_of_pages: 3397,
        },
        {
            id: 2,
            book_name: 'Grumpy Bear',
            author_name: 'Mike Scott',
            number_of_pages: 4467,
        },
        {
            id: 3,
            book_name: 'Jungle Josh',
            author_name: 'Fred Humphry',
            number_of_pages: 3397,
        },
        {
            id: 4,
            book_name: 'Forest gump',
            author_name: 'Mike Scott',
            number_of_pages: 4467,
        },
    ],
});

export const mutations = {
    // User Mutations
    LOGIN: (state: { user: Object }, data: Object) => {
        state.user = data;
    },
    LOGOUT: (state: { user: Object }, data: Object) => {
        state.user = {};
    },

    // Authors Mutations
    ALL_AUTHORS: (state: { authors: any[] }, data: any) => {
        state.authors = data;
    },
    ADD_AUTHOR: (state: { authors: any[] }, data: Object) => {
        state.authors.unshift(data);
    },
    DELETE_AUTHOR: (state: { authors: any[] }, data: Object) => {
        state.authors.splice(state.authors.indexOf(data), 1);
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
