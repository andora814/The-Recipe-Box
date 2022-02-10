<template>
    <div>This is Home.
    <input placeholder="Search food" name="food_search" type="food_search" v-on:input="handleFormChange" class="food-search"/>
            <div>
                <!-- <div> {{ food.name }} </div> -->
                <div v-for="food in food_search" :key="food.id">
                    <div> {{ food.name }} </div>
                    <button @click="SelectFood(food.name)">Select food</button>
                </div>
            </div>
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
        food_search: [],
        show_food_search: false
    }),
    mounted() {
  
    },
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
            if(e.target.value.length >= 3) {
                this.show_food_search=true
                this.ExternalFoodSearch(this.food_search)
            }
        },
        async ExternalFoodSearch (keyword) { 
            const res = await axios.get(`https://api.spoonacular.com/food/ingredients/search?query=${keyword}&number=20&sort=calories&sortDirection=desc&apiKey=9e2e99bbc2e8487baf824d1acd1621e9`);
            this.food_search = res.data.results
            console.log(this.food_search)
        },
        async SelectFood (food_name) {
            await axios.post(`http://localhost:8000/ingredients/`, {
            "name": food_name,
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            this.show_food_search=false
        }
    }
}
</script>

<style scoped>

</style>