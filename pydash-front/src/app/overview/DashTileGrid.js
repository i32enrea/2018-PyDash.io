import React, {Component} from 'react';
import './overview.css';
import Grid from 'material-ui/Grid';
import DashTile from './DashTile';
import { withStyles } from 'material-ui/styles';
import axios from 'axios';

const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing.unit * 2,
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
});


// Transforms a hashmap of key-value pairs into an array of {x: key, y: value} objects.
function dict_to_xy_arr(dict){
    let res =  Object.entries(dict).map(function([key, value]){
        return {x: key, y: value}
    });
    console.log('dict_to_xy_array', res);
    return res;
}

/* function destringify_date_keys(dict){
 *     let res =  Object.entries(dict).map(function([key, value]){
 *         let obj = {}
 *         obj[new Date(key)] = value;
 *         return obj;
 *     })
 *     .reduce((acc, kv) => Object.assign(acc, kv), {})
 *     console.log('destringify_date_keys', res);
 *     return res;
 * }
 * */

class DashTileGrid extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: props.username,
            dashboards: [],
        };
    }

    /*componentDidMount() {
        axios('http://localhost:5000/api/dashboards/123', {
            method: 'get',
            withCredentials: true
        }).then((response) => {
            console.log('success', response);
            this.setState(prevState =>{
                let newState = prevState;
                newState.total_visits = "" + response.data.aggregates.total_visits;
                newState.visits_per_day = dict_to_xy_arr(response.data.aggregates.visits_per_day)
                console.log(newState)

                return newState;
            })
        }).catch((error) => {
            console.log('error', error);

            /* this.setState(prevState =>{
             *     let newState = prevState;
             *     newState.total_visits = "" + mock_data.aggregates.total_visits;
             *     newState.visits_per_day = dict_to_xy_arr(mock_data.aggregates.visits_per_day)
             *     console.log(newState)

             *     return newState;
             * })
             */
        /*});
    }*/
    
    componentDidMount() {
      axios('http://localhost:5000/api/dashboards', {
        method: 'get',
        withCredentials: true
      }).then((response) => {
        console.log('found some data', response);
        
        
        this.setState(prevState => {
          let newState = prevState;
          newState.dashboards = response.data;
          
          console.log(newState);
          
          return newState;
        });
      }).catch((error) => {
        console.log('error', error);
      });
    }
 
    render() {
        const {classes} = this.props;
        
        let tiles = [];
        
        for (let i in this.state.dashboards) {
          let id = this.state.dashboards[i].id;
          let url = this.state.dashboards[i].url;
          tiles.push(<DashTile title={url} dashboard_id={id} xs={12} />);
        }

        return(
            <Grid container spacing={24} className={classes.root}>

                {/* For each found dashboard for username */}
                {tiles}
                    
            </Grid>
        );
    }
}

export default withStyles(styles)(DashTileGrid);