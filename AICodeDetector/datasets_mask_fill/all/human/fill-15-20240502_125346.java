// An activity which handles listening to AccountManager changes , or AuthenticatorActivity if no account are available
// Also hanldes an activity which provides an Otto bus, and provides a subscription to observables 
// while listening to activity lifecycle
@SuppressLint("Registered") public class BaseActivity extends FragmentActivity
    implements AccountManager.OnAccountChangeObserver {  @Inject AppContainer appContainer;
  @Inject ScopedBus bus;
  @Inject AccountManager accountManager;

  private ViewGroup container;
  private ObjectGraph activityGraph;

  private SubscriptionManager<Activity> subscriptionManager;

  @Override protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);    buildActivityGraphAndInject();

    // Inject any extras
    Dart.inject(this);
  }

  private void buildActivityGraphAndInject() {
   // Create the app object graph, used by .plus-ing our modules //     objectGraph = Dart.inject(this, application graph.
   get())
        App app = App.get(this);
 