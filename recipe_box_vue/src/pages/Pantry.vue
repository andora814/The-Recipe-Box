<template>
<div class="body">
    <div class="search-container">
        <input placeholder="🔍" name="search_word" type="food_search" v-on:input="handleFormChange" class="food-search"/>
                <div class="search-container">
                    <div v-if="show_food_search" class="suggestions-container">
                        <div v-for="food in food_search" :key="food.id" class="suggestions">
                            <div @click="SelectFood(food.name)"> {{ food.name }} </div>
                        </div>
                    </div>
                </div>
        <button @click="ExternalFoodSearch(search_word)">Add ingredient</button>
    </div>
    <div>
        <div v-for="ingredient in all_ingredients" :key="ingredient.id">
            {{ ingredient }}
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
            let array = []
            let data =[]
            const response = await axios.get('http://localhost:8000/ingredients/'
            )
            data = response.data
            for(let i=0; i<data.length; i++) {
                array.push(data[i].name)
            }
            this.all_ingredients = array.sort()
        }
    }
}
</script>

<style scoped>
.suggestions {
    cursor: pointer;
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
    position: absolute;
    top: 53px;
    left: 10px;
}

.search-container {
    display: flex;
    align-items: center;
}
.body {
    align-items: center;
}

.api-list {
    position: absolute;

}

</style>