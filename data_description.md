### Data Dictionary

Some column names may differ slightly, and some may be missing.

- `pointId`: Character point ID
- `setNumber`: Set Number
- `set`: Set Number
- `game`: Game Number
- `point`: Point number in a game (always starts at 1)
- `serve_num`: Serve Number (1,2). Lets are not tracked.
- `serverId`: 'Server ID
- `returnerId`: Returner ID
- `scorerId`: Point Winner ID (either serverID or returnerID)
- `court_side`: Serve Court ('AdCourt' or 'DeuceCourt')
- `serve_speed_kph`: Serve Speed in Kilometers per Hour
- `serve_type`:'Flat', “Pronated”, “Slice”, “Unclassified”
- `(x,y,z)`: Location of where the ball is according to hit and order.
- `position`: Where the ball was measured
- `order`: Ordering of the event within a point (starts at 0)
- `rally_length`: Length of rally (including serve)
- `point_end_type`: How did rally end?
  Ex: Fault, Unforced/Forced error, Winner
- `error_type`: If point ended in an error, which type?
  Ex: Net, Wide, Long
- `trapped_by_net`: *I think* Boolean for whether shot was net error?
- `last_troke`: Type of stroke on last shot of rally.
  Ex: Ground, Passing, Drop.
  “Last shot” means any last recorded shot (winner, error, etc)
- `last_hand`: Handedness on last shot.
- `last_stroke_net_height_m`: Ball height at net on last shot of rally (in metres).
- `winner_placement`: Cross Court or Down the Line
- `unforcedErrorPlacement`: If shot error, what type?
  Wide, Net, Long.
  This is the same as `error_type`?
- `is_break_point`: Boolean
- `is_break_point_converted`: Boolean
- `runAroundForeHand`: Boolean
- `(x,y,z`: coordinates of serve ball as it reached the net
- `spin`: Ball rpm on last rally shot
