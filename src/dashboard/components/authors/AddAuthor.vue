<template>
    <div>
        <b-button v-b-modal.modal-3 class="bg-primary ml-2 w-100">Add Author</b-button>

        <b-modal id="modal-3" title="Add Author">
            <b-form @submit="onSubmit">
                <b-form-group id="input-group-1" label="Author Name:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.author_name"
                        placeholder="Enter author name"
                        required
                    ></b-form-input>
                </b-form-group>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'AddAuthor',
    data() {
        return {
            form: {
                author_name: '',
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
