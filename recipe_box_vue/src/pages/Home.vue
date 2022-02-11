<template>
    <div>
        <h1>Search your recipe box</h1>
    <input placeholder="Enter food name" name="search_input" type="text" v-on:input="handleSearchChange" class="title-field"/>
    <button @click="filterRecipes" :disabled="search_disabled">Search Recipe Box</button>
    <button @click="clearSearch">Clear Search</button>
    </div>
</template>

<script>


export default {
    name: 'Home',
    components: {

    },
    data: () => ({
       
    }),
    mounted() {
        
    },
    methods: {
        
    }
}
</script>

<style scoped>


</style>