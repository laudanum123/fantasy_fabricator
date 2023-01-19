<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Dungeon Master</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/adventure_builder" class="nav-link">Adventure Builder</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/campaign_manager" class="nav-link">Campaign Manager</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/character_generator" class="nav-link">Character Generator</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/community_support" class="nav-link">Community Support</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/encounter_builder" class="nav-link">Encounter Builder</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/map_generator" class="nav-link">Map Generator</router-link>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>
