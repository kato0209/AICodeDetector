import org.apache.commons.math3.fitting.WeightedObservedPoints;
import org.apache.commons.math3.fitting.SimpleCurveFitter;
import org.apache.commons.math3.fitting.CurveFitter;
import org.apache.commons.math3.analysis.function.Logistic;

public class LogisticRegression {
    public static void main(String[] args) {
      <extra_id_0> // Generate <extra_id_1> data
  <extra_id_2>     WeightedObservedPoints obs = new WeightedObservedPoints();
        obs.add(1, 0.1);
 <extra_id_3>      obs.add(2, 0.2);
        obs.add(3, 0.3);
       <extra_id_4> 0.4);
 <extra_id_5>  <extra_id_6>   obs.add(5, 0.5);

        // Fit the data to a logistic function
     <extra_id_7>  CurveFitter<Logistic.Parametric> fitter = SimpleCurveFitter.create(new Logistic.Parametric(), obs.toList());
        <extra_id_8> = fitter.fit();

   