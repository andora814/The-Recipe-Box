<template>
    <div id="recipeform">
        <div class="form-container">
            <form @submit="handleSubmit">
                <div class="flex">
                    <h5>Add a new recipe</h5>
                    <input placeholder="Title" name="title" type="recipe_title" v-on:input="handleFormChange"/>
                    <input placeholder="Total minutes" name="ready_in_minutes" type="ready_in_minutes" v-on:input="handleFormChange"/>
                    <input placeholder="# of Servings" name="servings" type="servings" v-on:input="handleFormChange"/>
                    <input placeholder="Image URL" name="image" type="image_url" v-on:input="handleFormChange"/>
                    <input placeholder="Summary" name="summary" type="summary" v-on:input="handleFormChange"/>
                    <input placeholder="Step #" name="number" type="number" v-on:input="handleFormChange"/>
                    <input placeholder="Instructions" name="step" type="step" v-on:input="handleFormChange"/>
                    <input placeholder="Source" name="source" type="source" v-on:input="handleFormChange"/>
                    <button class="btn" type="submit">Submit Recipe</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AddRecipe',
    data: () => ({
        title: '',
        ready_in_minutes: 0,
        servings: 0,
        source_url: '',
        image: '',
        summary: '',
        source: '',
        number: 0,
        step: '',
        new_recipe: {}
    }),
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
        },
        async handleSubmit(e) {
            e.preventDefault()
            const recipe_response = await axios.post(`http://localhost:8000/recipes/`, {
                "title": this.title,
                "ready_in_minutes": this.ready_in_minutes,
                "servings": this.servings,
                "source_url": this.source_url,
                "image": this.image,
                "summary": this.summary,
                "source": this.source
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            this.$router.push(`/recipes/${recipe_response.data.id}`)
            console.log(recipe_response.data)
            this.new_recipe=recipe_response.data
            const instruction_response = await axios.post(`http://localhost:8000/instructions/`, {
                "recipe_id": this.new_recipe.id,
                "name": "test name string",
                "number": this.number,
                "step": this.step,
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            console.log(instruction_response)
        }
    }
}



</script>

<style scoped>
    h3 {
        color: #80cbc4;
    }
    input {
        width: 500px;
        height: 60px;
        margin: 10px;    
    }
    .flex {
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .btn {
        width: 509px;
        margin: 10px; 
    }
</style>