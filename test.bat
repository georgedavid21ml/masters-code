asci2gdf -o field_map(100-95-0).gdf 100-95-0(4000).txt
gpt -o test_particle.gdf test_particle.in
gdftrans -o traj.gdf test_particle.gdf time x y z Bx By Bz G
gdfa -o std.gdf test_particle.gdf time stdx stdz avgz nemixrms nemizrms numpar


gdf2a -o 100-95-0(q=0.01pC) std.gdf