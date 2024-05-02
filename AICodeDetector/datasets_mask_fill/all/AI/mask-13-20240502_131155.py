class FeedForwardNetwork(nn.Module):
  <extra_id_0> def <extra_id_1> hidden_dim, output_dim):
    <extra_id_2>   super(FeedForwardNetwork, self).__init__()
     <extra_id_3>  self.layer1 = nn.Linear(input_dim, hidden_dim)
       <extra_id_4> = nn.ReLU()
   <extra_id_5>    self.layer2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
      <extra_id_6> x = self.layer2(x)
        return x
