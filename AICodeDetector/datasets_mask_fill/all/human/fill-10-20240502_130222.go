/**
一个用golang写的日历，有公历转农历，农历转公历，节气，干支，星座，生肖等功能
中国的农历历法综合了太阳历和月亮历,为中国的生活生产提供了重要的帮助,是中国古人智慧与中国传统文化的一个重要体现

程序比较准确的计算出农历与二十四节气(精确到分),时间限制在-1000至3000年间,在实际使用中注意限制年份
*/

package gocalendar

import (
	"errors"
	"fmt"
	"math"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"
)

const Author = "liujiawm@gmail.com"
const Version = "0.1"

// type SolarTermItem struct 节气
type SolarTermItem struct {
	Index int        `json:"index"` // 节气索引
	Name  string    `json:"name"`  // 节气名称
	Time  *time.Time `json:"time"` // 定节气时间
}

// type yearSolarTermTemp struct
type yearSolarTermTemp struct {
	data map[int][]*SolarTermItem
	mu   sync.RWMutex
}

// type StarSignItem struct 星座单元
type StarSignItem struct {
	Index int   `json:"index"` // 星座索引
	Name  string `json:"name"`  // 星座名称
}

// type FestivalItem struct type FestivalItem struct {
	Show      []string `json:"show"` // 在日历表上显示的节日
	Secondary []string `json:"scdr"` // 其它次要节日
}

// type yearFestivalTemp struct type yearFestivalTemp struct {
	data map[int]map[string][]string
	mu   sync.RWMutex
}

// type CalendarItem struct 日历单元
type CalendarItem struct {
	Time         *time.Time     `json:"time"`  