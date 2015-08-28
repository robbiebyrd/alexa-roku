from roku import Roku
import pprint

roku = Roku('192.168.3.22')
roku.home()
roku.search()
roku.left()
roku.select()
roku.literal('  michael keaton')