<template>
<div class="body">
    <div class="search-container">
        <input placeholder="Enter ingredient" name="search_word" type="food_search" v-on:input="handleFormChange" class="food-search"/>
                <div class="search-container">
                    <div v-if="show_food_search" class="suggestions-container">
                        <div v-for="food in food_search" :key="food.id" class="suggestions">
                            <div @click="SelectFood(food.name)"> {{ food.name }} </div>
                        </div>
                    </div>
                </div>
        <button @click="ExternalFoodSearch(search_word)">Search for new ingredient</button>
    </div>
    <div class="ingredient-list">
        <div v-for="ingredient in all_ingredients" :key="ingredient.id">
            {{ ingredient }}
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

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
    background-color: #f4aa09;
    border-radius: 5px;
}

.suggestions-container {
    position: absolute;
    background-color: #017754;
    border-radius: 0 0px 10px 10px;
    align-items: center;
    display: flex;
    flex-direction: column;
    width: 200px;
    position: absolute;
    top: 110px;
    left: 30px;
}

.search-container {
    display: flex;
    align-items: center;
    margin: 10px;
}
.body {
    align-items: center;
    background-color: #03195a;
    color: white;
    height: 100vh;
    background-repeat: no-repeat;
    background-blend-mode: screen;
    background-size: cover;
    padding: 10px;
}

.ingredient-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    font-size: 25px;
}
button {
    height: 30px;
    margin: 10px;
    outline-style: solid;
    outline-color: white;
    background-color: transparent;
    border: none;
    color: white;
}
button:hover {
    background-color: white;
    color: #03195a;
}
input {
    height: 30px;
    width: 300px;
    margin: 10px;
    outline: none;
}
</style>