export const state = () => ({
    user: {},
});

export const mutations = {
    // User Mutations
    LOGIN: (state: { user: any }, data: any) => {
        state.user = data;
        localStorage.setItem('access_token', data.access_token);
    },
    LOGOUT: (state: { user: Object }) => {
        state.user = {};
        localStorage.removeItem('access_token');
    },
};
