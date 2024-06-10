# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits







class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # ball distance away from foe goal
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # me distance from ball
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # me distance from ball
        d3 = abs(self.me.location.y - self.ball.location.y)
        # me distance from foe
        d4 = abs(self.me.location.y - self.foes[0].location.y)
        # distance from foe to ball
        d5 = abs(self.foes[0].location.y - self.ball.location.y)
        # distance ball from my from my goal
        d6 = abs(self.ball.location.y - self.foe_goal.location.y)
        
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post - 10, self.friend_goal.left_post + 10)
        }
        hits = find_hits(self, targets)
        is_in_front_of_ball = d1 > (d2 + 100)
        is_behind_ball = d2 < d1
        is_away_from_ball =  d3 > 50
        closer_to_foe = d4 > (d3 + 5)
        ball_in_my_half = d5 < d3
        low_boost = 10
        

      
        if self.intent is not None:
            return
        
        if self.set_intent(kickoff()):
            return
        
        
        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.left_post))
            return
            
        if is_behind_ball: 
            
            self.set_intent(find_hits(self, targets))
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal' ][0])
            return
       
        if len(hits['away_from_our_net']) > 0:
             self.set_intent(hits['away_from_our_net'][0])
             return
        
        target_boosts = self.get_closest_large_boost()
        
        if self.me.boost is low_boost and target_boosts is not None and is_behind_ball:
             self.set_intent(goto(target_boosts.location))
             return

        if self.me.supersonic and closer_to_foe:
            self.set_intent(goto(self.foes[0].location)) 
            return
        
        if self.set_intent is None:
            return

      
    
        
     
        

   



        