// An activity which handles listening to AccountManager changes <extra_id_0> AuthenticatorActivity if no account are available
// Also hanldes <extra_id_1> provides an Otto bus, <extra_id_2> subscription to observables 
// while listening to activity lifecycle
@SuppressLint("Registered") public class BaseActivity extends FragmentActivity
    implements <extra_id_3>  @Inject AppContainer appContainer;
  @Inject ScopedBus bus;
  @Inject AccountManager accountManager;

  private ViewGroup container;
  private ObjectGraph activityGraph;

  private SubscriptionManager<Activity> subscriptionManager;

  @Override protected void onCreate(Bundle savedInstanceState) {
   <extra_id_4>    buildActivityGraphAndInject();

    // Inject any extras
    Dart.inject(this);
  }

  private void buildActivityGraphAndInject() {
   <extra_id_5> Create the <extra_id_6> by .plus-ing our modules <extra_id_7> application graph.
   <extra_id_8> app = App.get(this);
 