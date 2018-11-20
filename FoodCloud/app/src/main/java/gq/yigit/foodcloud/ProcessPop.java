package gq.yigit.foodcloud;

import android.app.Activity;
import android.app.ListActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

public class ProcessPop extends Activity {
    public JSONObject json_proc;
    public String[] processes;
    public ListView proc_lst;
    public TextView proc_place;
    public TextView proc_ok;
    public ImageView proc_ok_img;
    public boolean proc_prob;
    private static final String TAG = "MainActivity";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Bundle extras = getIntent().getExtras();
        setContentView(R.layout.activity_process_pop);
		proc_lst = (ListView)findViewById(R.id.proc_lst);
		proc_place = (TextView)findViewById(R.id.processed_in);
		proc_ok = (TextView)findViewById(R.id.proc_ok);
		proc_ok_img = (ImageView) findViewById(R.id.proc_ok_img);

        if (extras != null) {
            try {
                json_proc = new JSONObject(extras.getString("key"));
            }catch(JSONException e){
                Log.d(TAG,"An error occured with json!");
            }
            }
        super.onCreate(savedInstanceState);
        try {
            processes = json_proc.get("Processes").toString().split(",");
			proc_place.setText((String)json_proc.get("Location"));
			proc_prob = (boolean)json_proc.get("Problematic");
        }catch(JSONException e){
            Log.d(TAG,"An error occured with json!");
        }
        String process_print = new String();
        for (int i=0; i<processes.length;i++){
        	process_print += ((i+1) +".    " + processes[i] + "\n");
		}
		ArrayAdapter<String> proc_adapter = new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,processes);
        proc_lst.setAdapter(proc_adapter);
		Log.d(TAG,process_print);
		if(proc_prob){
			proc_ok_img.setImageResource(R.mipmap.warning);
			proc_ok.setText("Warning, there was an error in the processing of this product. We recommend that you don't consume it!");
		}else{
			proc_ok_img.setImageResource(R.mipmap.check);
			proc_ok.setText("This product did not have any problems during processing. It is safe to consume!");
		}

        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);
        int width = dm.widthPixels;
        int height = dm.heightPixels;
        getWindow().setLayout((int)(width*0.8), (int)(height*0.53));
    }
}
