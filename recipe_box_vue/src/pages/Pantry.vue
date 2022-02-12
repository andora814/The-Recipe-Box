<template>
    <div class="search-container">
    <input placeholder="Search external API" name="search_word" type="food_search" v-on:input="handleFormChange" class="food-search"/>
            <div>
                <div v-if="show_food_search" class="suggestions-container">
                    <div v-for="food in food_search" :key="food.id" class="suggestions">
                        <div @click="SelectFood(food.name)"> {{ food.name }} </div>
                    </div>
                </div>
            </div>
    <button @click="ExternalFoodSearch(search_word)">Search external API</button>
    <div>
        <div v-for="ingredient in all_ingredients" :key="ingredient.id">
            {{ ingredient.name }}
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'

// const API_KEY = process.env.VUE_APP_SPOONACULAR_KEY;
export default {
    name: 'Pantry',
    components: {

    },
    data: () => ({
        food_search: [],
        show_food_search: false,
        search_word: '',
        all_ingredients: []
    }),
    mounted() {
        this.GetAllFood()
    },
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
        },
        async ExternalFoodSearch (keyword) { 
            this.show_food_search = true
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
            window.location.reload()
        },
        async GetAllFood() {
            const response = await axios.get('http://localhost:8000/ingredients/'
            )
            this.all_ingredients =response.data.sort()
        }
    }
}
</script>

<style scoped>
.suggestions {
    cursor: pointer
}

.suggestions:hover {
    background-color: white;
    border-radius: 5px;
}

.suggestions-container {
    position: absolute;
    background-color: green;
    border-radius: 0 0px 10px 10px;
    align-items: center;
    display: flex;
    flex-direction: column;
    width: 200px;
}

</style>