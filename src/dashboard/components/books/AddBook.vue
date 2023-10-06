<template>
    <div>
        <b-button v-b-modal.modal-1 class="bg-primary ml-2 w-100">Add Book</b-button>

        <b-modal id="modal-1" title="Add New Book">
            <b-form @submit="onSubmit">
                <b-form-group id="input-group-1" label="Book Name:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.book_name"
                        placeholder="Enter book name"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-2" label="Author Name:" label-for="input-2">
                    <b-form-input
                        id="input-2"
                        v-model="form.author_name"
                        placeholder="Enter author name"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-3" label="Number of pages:" label-for="input-3">
                    <b-form-input
                        type="number"
                        id="input-3"
                        v-model="form.number_of_pages"
                        placeholder="Enter number of pages"
                        required
                    ></b-form-input>
                </b-form-group>

                <!-- <b-button type="submit" variant="primary">Submit</b-button> -->
            </b-form>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'AddBook',
    data() {
        return {
            form: {
                book_name: '',
                author_name: '',
                number_of_pages: 0,
            },
        };
    },
    methods: {
        onSubmit(event) {
            event.preventDefault();
            console.log(event);
        },
    },
};
</script>

<style></style>
