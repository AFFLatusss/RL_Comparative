for i_episode in range(5):
#     observation = env.reset()
#     print(1)
#     for t in range(100):
#         env.render()
#         # print(observation)
#         action = env.action_space.sample()
#         # print(action)
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
# env.close()