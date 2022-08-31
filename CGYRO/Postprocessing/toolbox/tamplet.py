from get_info_obj import sim_info

# load the cgyro directory
sim_dir = './../reg08/'

w=1. # read last portation of the time w=0.1 ==> last 10% of time  

sim_obj=sim_info(sim_dir,w)

print(sim_obj.dic)