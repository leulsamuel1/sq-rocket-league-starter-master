# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
     #This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        



        if self.is_in_front_of_ball():
            
            self.set_intent(goto(self.friend_goal.location))
            return
        
        if self.me.boost == 0:
            self.set_intent(goto(self.get_closest_large_boost()))
            location1 = (self.ball.location - self.foe_goal.location).magnitude()
            location2 = (self.me.location - self.foe_goal.location).magnitude()
            if location1 > location2:
                return short_shot
        if self.me.boost >40:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        
        
        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            return




        #if len(available_boosts) > 0:
         #   self.set_intent(goto(available_boosts[0].location))
          #  print("going for boost", available_boosts[0].index)
         #   return








       # targets = {
            #"at_opponent_goal": (self.foe_goal.left_post, self.foe_goal.right_post),
            #"away_from_our_net": (self.friend_goal.right_post, self.friend_goal.left_post)
       # }
        #hits= find_hits(self,targets)
        #if len(hits["at_opponent_goal"]) > 0:
            #self.set_intent(hits["at_opponent_goal"][0])
            #return
        #if len(hits[ "away_from_our_net"]) >0:
            #self.set_intent(hits["away_from_our_net"][0])
           # return


#if self.time % 2 == 0:
           # print(hits)

#class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    #def run(self):
        #if self.intent is not None:
            #return
        #d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        #d2 = abs(self.me.location.y - self.foe_goal.location.y)
        #is_in_front_of_ball = d1>d2
        #is_in_front_of_ball = False 
        #if self.kickoff_flag:
            #self.set_intent(kickoff())
            #return
        #if is_in_front_of_ball:
            #self.set_intent(goto(self.friend_goal.location))
            #return
        #self.set_intent(short_shot(self.foe_goal.location))

        

