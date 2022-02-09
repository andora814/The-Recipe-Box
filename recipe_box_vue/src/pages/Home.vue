<template>
    <div>This is Home.
    <input placeholder="Search food" name="food_search" type="food_search" v-on:input="handleFormChange" class="food-search"/>
    </div>
</template>

<script>
import axios from 'axios'
// const API_KEY = process.env.VUE_APP_SPOONACULAR_KEY;
export default {
    name: 'Home',
    components: {

    },
    data: () => ({
        food_search: ''
    }),
    mounted() {
  
    },
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
            this.ExternalFoodSearch(this.food_search)
        },
        async ExternalFoodSearch (keyword) { 
            const res = await axios.get(`https://api.spoonacular.com/food/ingredients/search?query=${keyword}&number=20&sort=calories&sortDirection=desc&apiKey=9e2e99bbc2e8487baf824d1acd1621e9`);
            console.log(res.data.results)
        }
    }
}
</script>

<style scoped>

</style>