# Class containing a possible keyboard actions
class KeyboardCallbacks(object):

    # Close program
    def quitOut(self, event, window):
        window.destroy()
        #print("Quit Out")

    # Player Movement
    def playerMove(self, event, player):
        player.move(event.char)