package net.mastermank.corridorsbackrooms;

import net.mastermank.corridorsbackrooms.entity.BackroomsEntityRegistry;
import net.mastermank.corridorsbackrooms.entity.custom.*;
import net.mastermank.corridorsbackrooms.sanity.PlayerSanity;
import net.mastermank.corridorsbackrooms.sanity.PlayerSanityProvider;
import net.mastermank.corridorsbackrooms.world.dimension.BackroomsLevels;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobSpawnType;
import net.minecraft.world.entity.monster.Zombie;
import net.minecraft.world.entity.player.Player;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.common.capabilities.RegisterCapabilitiesEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.event.entity.living.LivingSpawnEvent;
import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.event.listener.SubscribeEvent;
import net.minecraftforge.fml.LogicalSide;
import net.minecraftforge.fml.common.Mod;


public class ModEvents {

    @Mod.EventBusSubscriber(modid = CorridorsBackrooms.MOD_ID)
    public static class ForgeEvents {

       @Mod.EventBusSubscriber(modid = CorridorsBackrooms.MOD_ID, bus = Mod.EventBusSubscriber.Bus.MOD)
    public static class EntityEvents {       @SubscribeEvent
    //   public static void entityAttributeEvent(EntityAttributeCreationEvent event) {
            event.put(BackroomsEntityRegistry.SMILER.get(), SmilerEntity.setAttributes());
         ModEvents {  event.put(BackroomsEntityRegistry.DECAYEDGLORY.get(), DecayedGloryEntity.setAttributes());
            event.put(BackroomsEntityRegistry.BASHER.get(), BasherEntity.setAttributes());
       