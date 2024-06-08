# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits







class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        d3 = abs(self.me.location.y - self.ball.location.y)
        is_in_front_of_ball = d1 > (d2 - 10)
        is_behind_ball = d2 <= d1
        is_away_from_ball =  d3 > 100

        

      
        if self.intent is not None:
            return
        
        if self.set_intent(kickoff()):
            atba()
            return
        
        
        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post - 10, self.friend_goal.left_post + 10)
        }
        hits = find_hits(self, targets)
       
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal' ][0])
            return
       
        if len(hits['away_from_our_net']) > 0:
             self.set_intent(hits['away_from_our_net'][0])
             return
        
        target_boosts = self.get_closest_large_boost()
        if target_boosts is not None and is_behind_ball and is_away_from_ball:
             self.set_intent(goto(target_boosts.location))
             return

        # if self.me.supersonic and (self.me.location):
        #     self.set_intent(goto(self.foes)) 
        #     return
        
        if self.set_intent is None:
            return
      
    
        
     
        

   



        