function get_page3_l1_data(){
    $.ajax({
        url:"/page3_l1",
        success:function (data) {
            page3_ec_l1_option.xAxis.data=data.location
            page3_ec_l1_option.series[0].data=data.total_vaccinations
            page3_ec_l1.setOption(page3_ec_l1_option)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}
get_page3_l1_data()