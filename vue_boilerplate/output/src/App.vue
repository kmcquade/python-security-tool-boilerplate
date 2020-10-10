<template>
    <div id="main">

        <!--Navigation bar-->
        <b-navbar toggleable="md" variant="faded">
            <b-navbar-brand @click="activeSection = 0" href="#">
                vue_boilerplate
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item
                        :active="activeSection === 'summary'"
                        @click="activeSection = 0"
                        href="#">Summary
                    </b-nav-item>
                    <b-nav-item disabled>Disabled</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-text><strong>MoreMetadata:</strong> {{ more_metadata }}</b-nav-text>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>

        <!--Content and Components-->
        <b-container class="mt-3 pb-3 report">
            <b-tabs v-model="activeSection" nav-class="d-none">
                <b-tab key="summary">
                    <h1>Example Table Display</h1>
                    <TableReport v-bind:report_data="report_data"/>
                </b-tab>
            </b-tabs>
        </b-container>

        <!--Footer-->
        <b-container>
            <b-row class="mt-5">
                <b-col class="text-center text-muted">
                    Report Generated: {{ report_generated_time }} &diamond;
                    Version:
                    <b-link href="https://github.com/kmcquade/vue_boilerplate">{{ version }}</b-link>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import TableReport from './components/TableReport.vue'

    const sampleData = require('./sampleData');


    // eslint-disable-next-line no-undef
    if ((process.env.NODE_ENV === "development") || (isLocalExample === true)) {
        // eslint-disable-next-line no-undef
        console.log(`isLocalExample is set to: ${isLocalExample}`)
        console.log(`process.env.NODE_ENV: ${process.env.NODE_ENV}`)
        console.log(`Note: a report generated with the Python template will not have isLocalExample set to True, because that uses a separate template.html file, which has isLocalExample set to False.`)
        // eslint-disable-next-line no-unused-vars,no-undef
        report_data = sampleData.sample_data;
        // eslint-disable-next-line no-unused-vars,no-undef
        report_generated_time = "2020-09-01";
        // eslint-disable-next-line no-unused-vars,no-undef
        version = "0.0.1";
    } else {
        console.log(`process.env.NODE_ENV: ${process.env.NODE_ENV}`)
        // eslint-disable-next-line no-undef
        console.log(`isLocalExample is set to: ${isLocalExample}`)
    }

    export default {
        name: 'App',
        components: {
            TableReport
        },
        data() {
            return {
                activeSection: 0,
                // eslint-disable-next-line no-undef
                report_data: report_data,
                // eslint-disable-next-line no-undef
                report_generated_time: report_generated_time,
                // eslint-disable-next-line no-undef
                version: version,
                more_metadata: "123456789012"
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
