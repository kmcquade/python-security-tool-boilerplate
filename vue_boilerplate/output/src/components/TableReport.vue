<template>
    <div>
        <b-container v-bind:id="'table-report'">
            <!-- User Interface controls -->
            <b-row>
                <b-col></b-col>
                <b-col></b-col>
                <b-col>
                    <b-form-group
                            label="Per page"
                            label-cols-sm="6"
                            label-cols-md="4"
                            label-cols-lg="3"
                            label-align-sm="right"
                            label-size="sm"
                            label-for="perPageSelect"
                            class="mb-0"
                    >
                        <b-form-select
                                v-model="perPage"
                                id="perPageSelect"
                                size="sm"
                                :options="pageOptions"
                        ></b-form-select>
                    </b-form-group>
                </b-col>

            </b-row>
                <b-table
                    :items="report_data"
                    :fields="fields"
                    small
                    :sort-by.sync="sortBy"
                    :sort-desc.sync="sortDesc"
                    :current-page="currentPage"
                    :per-page="perPage"
                    responsive="sm"
                >
                </b-table>
        </b-container>
    </div>
</template>

<script>
    export default {
        name: "TableReport",
        props: {
            report_data: {
                type: Array
            }
        },
        data() {
            return {
                sortBy: "first_name",
                sortDesc: false,
                totalRows: 1,
                currentPage: 1,
                perPage: 20,
                pageOptions: [5, 10, 15, 20, 50, 100],
                fields: [
                    {key: 'first_name', sortable: true},
                    {key: 'last_name', sortable: true},
                    {key: 'city', sortable: true}
                ],
            }
        }
    }
</script>

<style scoped>

</style>
