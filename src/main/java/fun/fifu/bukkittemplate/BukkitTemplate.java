package fun.fifu.bukkittemplate;

import com.alkaidmc.alkaid.bukkit.event.AlkaidEvent;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class BukkitTemplate extends JavaPlugin implements Listener {
    public static BukkitTemplate plugin;

    @Override
    public void onLoad() {
        plugin = this;
    }

    @Override
    public void onEnable() {
        new AlkaidEvent(plugin).simple()
                // 监听的事件
                .event(PlayerJoinEvent.class)
                // 事件处理器
                .listener(event -> {
                    event.getPlayer().sendMessage("欢迎光临~");
                })
                // 事件优先级
                .priority(EventPriority.HIGHEST)
                // 忽略取消标志位
                .ignore(false)
                // 将事件注册到 Bukkit 事件系统
                .register();

    }

    @Override
    public void onDisable() {
        getLogger().info("感谢使用本插件");
    }

}
