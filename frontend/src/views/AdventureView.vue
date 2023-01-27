<template>
    <div class="container my-5">
        <div v-if="adventure" class="row justify-content-center">
            <div class="col-md-8">
                <div class="d-flex justify-content-between">
                    <h2 class="text-center">{{ adventure.AdventureTitle }}</h2>
                    <router-link :to="{ name: 'campaign manager' }" class="btn btn-primary">Back to
                        Overview</router-link>
                </div>
                <hr>
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">Adventure Hook</h4>
                        <p class="card-text">{{ adventure.AdventureHook }}</p>
                    </div>
                </div>
                <br>
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">Adventure NPCs</h4>
                        <p class="card-text">{{ adventure.AdventureNPCs }}</p>
                    </div>
                </div>
                <br>
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">Adventure Plot</h4>
                        <p class="card-text">{{ adventure.AdventurePlot }}</p>
                    </div>
                </div>
                <br>
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">Adventure Climax</h4>
                        <p class="card-text">{{ adventure.AdventureClimax }}</p>
                    </div>
                </div>
                <br>
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">Adventure Resolution</h4>
                        <p class="card-text">{{ adventure.AdventureResolution }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

.card:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>
<script>
import axios from 'axios';
const backendURL = 'http://localhost:5000';
export default {
    data() {
        return {
            adventure: null,
        }
    },
    mounted() {
        const path = `${backendURL}/get_adventures_from_db`;
        axios.get(path, { params: { id: this.$route.query.id } })
            .then(response => {
                this.adventure = response.data[0];
            })
            .catch(error => {
                console.log(error)
            })
    }
}
</script>
