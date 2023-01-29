<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Fantasy <br>Fabricator</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/adventure_builder' }">
                        <router-link to="/adventure_builder" class="nav-link">Adventure Builder</router-link>
                    </li>
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/adventure_manager' }">
                        <router-link to="/adventure_manager" class="nav-link">Adventure Manager</router-link>
                    </li>
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/character_generator' }">
                        <router-link to="/character_generator" class="nav-link">Character Generator</router-link>
                    </li>
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/community_support' }">
                        <router-link to="/community_support" class="nav-link">Community Support</router-link>
                    </li>
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/encounter_builder' }">
                        <router-link to="/encounter_builder" class="nav-link">Encounter Builder</router-link>
                    </li>
                    <li class="nav-item" :class="{ 'bg-secondary': $route.path === '/map_generator' }">
                        <router-link to="/map_generator" class="nav-link">Map Generator</router-link>
                    </li>
                </ul>
            </div>
        </nav>

    </div>
</template>
<style>
.nav_item {
    height: 100%;
    line-height: 100%;
}
</style>
