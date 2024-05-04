class FeedForwardNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(FeedForwardNetwork, self).__init__()
        self.layer1 = nn.Linear(input_dim, <extra_id_0>   <extra_id_1>   self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, output_dim)

  <extra_id_2> def forward(self, x):
       <extra_id_3> = self.layer1(x)
    <extra_id_4>   x = self.relu(x)
    <extra_id_5>   x = self.layer2(x)
      <extra_id_6> return x
