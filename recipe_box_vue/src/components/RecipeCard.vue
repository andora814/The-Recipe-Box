<template>
  <div class="recipe_container">
    <div class="container">
      <div> {{ recipe.title }} </div>
      <img :src="recipe.image" alt="recipe picture" :class="picclass" />
      <!-- <div v-if="showName" class="center" >{{ image_card.title }}</div> -->
    </div>
    <div @click="deleteRecipe" class="delBtn">x</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeCard',
  data: () => ({
    showName: false,
    picclass: 'normal'
  }),
  props: {
    recipe: Object
  },
  methods: {
    async deleteRecipe() {
        await axios.delete(`http://localhost:8000/recipes/${this.recipe.id}`, {
          auth: {
            username: 'recipeboxuser',
            password: 'recipe'
          }
        })
        this.$emit('handleDelete', this.recipe.id)
    }
}
}
</script>

<style scoped>

img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}

.container {
  position: relative;
  display: flex;
  justify-content: center;
}

.center {
  position: absolute;
  top: 50%;
  text-align: center;
  font-size: 22px;
  color: black
}

img { 
  width: 100%;
  height: auto;
}

.blur {
  opacity: 0.6;
}

.image_card_container {
  width: 300px;
  margin-bottom: 10px;
}

.delBtn {
  width: 100%;
  background-color: green;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 0 0 7px 7px
}

.delBtn:hover {
  background-color: red;
  color: white
}


</style>