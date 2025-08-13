import xbmc
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()

class PlaybackMonitor(xbmc.Player):
    def onPlayBackStarted(self):
        xbmc.sleep(1000)  # Let playback settle
        self.showSubtitles(True)
        xbmc.sleep(500)  # Wait for subtitles to possibly load

        if not self.getSubtitles():
            xbmcgui.Dialog().notification("AutoOnSubtitles", "No subtitles available", xbmcgui.NOTIFICATION_INFO, 5000)
            xbmc.log("[AutoOnSubtitles] No subtitles were found.", xbmc.LOGINFO)
        else:
            xbmc.log("[AutoOnSubtitles] Subtitles enabled.", xbmc.LOGINFO)

class ServiceMonitor(xbmc.Monitor):
    def __init__(self):
        super().__init__()
        self.player = PlaybackMonitor()

    def run(self):
        while not self.abortRequested():
            xbmc.sleep(1000)

if __name__ == '__main__':
    monitor = ServiceMonitor()
    monitor.run()
